""" convert various frictionless objects to
another format """

def convert_frictionless_to_jsonschema(frictionless_schema):
    """ converts a frictionless schema to jsonschema """
    
    frictionless_fields = list(frictionless_schema.get("fields"))
    assert frictionless_fields,"A frictionless schema MUST have a set of fields"


    # schema level properties

    ## jsonschema
    required = []
    # frictionless
    missing_values = frictionless_schema.get("missingValues",None)
    primary_keys = frictionless_schema.get("primaryKeys",[])

    # frictionless --> jsonschema per field
    jsonschema_properties = {}
    for field in frictionless_fields:

        jsonschema_properties[field["name"]] = prop = {}

        #base props
        if "description" in field:
            prop["description"] = field["description"]
        if "title" in field:
            prop["title"] = field["title"]
        if "example" in field:
            prop["example"] = field["example"]
        if "type" in field:
            if field["type"]!="any":
                prop["type"] = field["type"]
        
        

        # constraints
        constraints = field.get("constraints",{})
        if "enum" in constraints:
            type_mappings = {
                "integer":int,
                "number":float,
                "string":str
            }
            prop["enum"] = []
            for val in constraints["enum"]:
                if field.get("type","") in type_mappings:
                    coerced_val = type_mappings[field["type"]](val)
                    prop["enum"].append(coerced_val)
                else:
                    prop["enum"].append(val)


        if "pattern" in constraints:
            prop["pattern"] = constraints["pattern"] 

        if "minimum" in constraints:
            prop["minimum"] = constraints["minimum"]

        if "maximum" in constraints:
            prop["maximum"] = constraints["maximum"]


        # missing-ness and required
        if "required" in constraints or field["name"] in primary_keys:
            required.append(field["name"])
        elif missing_values:
            prop_with_missing = {"oneOf":[
                prop,{"enum":missing_values}
            ]}
            jsonschema_properties[field["name"]] = prop_with_missing

    jsonschema_schema = {
        "type":"object",
        "required":required,
        "properties":jsonschema_properties
    }

    schema = frictionless_schema
    for jsonprop in ["description","title","name"]:
        if schema.get(jsonprop):
            jsonschema_schema[jsonprop] = schema[jsonprop]

    return jsonschema_schema