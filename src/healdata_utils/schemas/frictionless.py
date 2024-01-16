healcsvschema = {
    "version": "0.2.0",
    "description": "\n"
    "\n"
    '!!! note "Highly encouraged"\n'
    "\n"
    "  Only `name` and `description` properties are required. \n"
    "  For categorical variables, `constraints.enum` and "
    "`enumLabels` (where applicable) properties are highly "
    "encouraged. \n"
    "  For studies using HEAL or other common data elements "
    "(CDEs), `standardsMappings` information is highly "
    "encouraged.\n"
    "  `type` and `format` properties may be particularly useful "
    "for some variable types (e.g. date-like variables)\n",
    "title": "HEAL Variable Level Metadata Fields",
    "fields": [
        {
            "name": "schemaVersion",
            "description": "The version of the schema used in agreed upon "
            "convention of major.minor.path (e.g., 1.0.2) \n"
            "\n"
            "NOTE: This is NOT for versioning of each "
            "indiviual data dictionary instance. \n"
            "Rather, it is the\n"
            "version of THIS schema document. See `version` "
            "property (below) if specifying the individual "
            "data dictionary instance\n"
            "version.\n"
            "\n"
            "If generating a vlmd document as a csv file, "
            "include this version in \n"
            "every row/record to indicate this is a schema "
            "level property \n"
            "(not applicable for the json version as this "
            "property is already at the schema/root "
            "level)\n",
            "examples": ["1.0.0", "0.2.0"],
            "type": "string",
            "constraints": {"pattern": "\\d+\\.\\d+\\.\\d+"},
        },
        {
            "name": "section",
            "description": "The section, form, survey instrument, set of "
            "measures  or other broad category used \n"
            "to group variables. Previously called "
            '"module."\n',
            "title": "Section",
            "examples": ["Demographics", "PROMIS", "Medical History"],
            "type": "string",
        },
        {
            "name": "name",
            "description": "The name of a variable (i.e., field) as it "
            "appears in the data. \n",
            "title": "Variable Name",
            "examples": ["gender_id"],
            "type": "string",
            "constraints": {"required": True},
        },
        {
            "name": "title",
            "description": "The human-readable title or label of the " "variable.\n",
            "title": "Variable Label (ie Title)",
            "examples": ["Gender identity"],
            "type": "string",
        },
        {
            "name": "description",
            "description": "An extended description of the variable. This "
            "could be the definition of a variable or the \n"
            "question text (e.g., if a survey). \n",
            "title": "Variable Description",
            "examples": [
                "The participant's age at the time of study " "enrollment",
                "What is the highest grade or level of school "
                "you have completed or the highest degree you "
                "have received?",
            ],
            "type": "string",
            "constraints": {"required": True},
        },
        {
            "name": "type",
            "description": "A classification or category of a particular "
            "data element or property expected or allowed "
            "in the dataset.\n",
            "title": "Variable Type",
            "type": "string",
            "constraints": {
                "enum": [
                    "time",
                    "geopoint",
                    "any",
                    "date",
                    "datetime",
                    "year",
                    "number",
                    "integer",
                    "duration",
                    "boolean",
                    "string",
                    "yearmonth",
                ]
            },
        },
        {
            "name": "format",
            "description": "Indicates the format of the type specified in "
            "the `type` property. \n"
            "Each format is dependent on the `type` "
            "specified. \n"
            "See "
            "[here](https://specs.frictionlessdata.io/table-schema/#types-and-formats) \n"
            "for more information about appropriate "
            "`format` values by variable `type`.\n",
            "title": "Variable Format",
            "type": "string",
        },
        {
            "name": "constraints.required",
            "description": "If this variable is marked as true, then this "
            "variable's value must be present\n"
            "(ie not missing; see missingValues). If marked "
            "as false or not present, then the \n"
            "variable CAN be missing.\n",
            "title": "Required variable",
            "type": "boolean",
        },
        {
            "name": "constraints.maxLength",
            "description": "Indicates the maximum length of an iterable "
            "(e.g., array, string, or\n"
            "object). For example, if 'Hello World' is the "
            "longest value of a\n"
            "categorical variable, this would be a "
            "maxLength of 11.\n",
            "title": "Maximum Length",
            "type": "integer",
        },
        {
            "name": "constraints.enum",
            "description": "Constrains possible values to a set of " "values.\n",
            "title": "Variable Possible Values",
            "examples": ["1|2|3|4|5", "Poor|Fair|Good|Very good|Excellent"],
            "type": "string",
            "constraints": {"pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$"},
        },
        {
            "name": "constraints.pattern",
            "description": "A regular expression pattern the data MUST "
            "conform to.\n",
            "title": "Regular Expression Pattern",
            "type": "string",
        },
        {
            "name": "constraints.maximum",
            "description": "Specifies the maximum value of a field (e.g., "
            "maximum -- or most\n"
            "recent -- date, maximum integer etc). Note, "
            "this is different then\n"
            "maxLength property.\n",
            "title": "Maximum Value",
            "type": "integer",
        },
        {
            "name": "constraints.minimum",
            "description": "Specifies the minimum value of a field.\n",
            "title": "Minimum Value",
            "type": "integer",
        },
        {
            "name": "enumLabels",
            "description": "Variable value encodings provide a way to "
            "further annotate any value within a any "
            "variable type,\n"
            "making values easier to understand. \n"
            "\n"
            "\n"
            "Many analytic software programs (e.g., "
            "SPSS,Stata, and SAS) use numerical encodings "
            "and some algorithms\n"
            "only support numerical values. Encodings (and "
            "mappings) allow categorical values to be "
            "stored as\n"
            "numerical values.\n"
            "\n"
            "Additionally, as another use case, this field "
            "provides a way to\n"
            'store categoricals that are stored as  "short" '
            "labels (such as\n"
            "abbreviations).\n"
            "\n"
            "This field is intended to follow [this "
            "pattern](https://specs.frictionlessdata.io/patterns/#table-schema-enum-labels-and-ordering)\n",
            "title": "Variable Value Encodings (i.e., mappings; value " "labels)",
            "examples": [
                "1=Poor|2=Fair|3=Good|4=Very good|5=Excellent",
                "HW=Hello world|GBW=Good bye world|HM=Hi, Mike",
            ],
            "type": "string",
            "constraints": {"pattern": "^(?:.*?=.*?(?:\\||$))+$"},
        },
        {
            "name": "enumOrdered",
            "description": "Indicates whether a categorical variable is "
            "ordered. This variable  is\n"
            "relevant for variables that have an ordered "
            "relationship but not\n"
            "necessarily  a numerical relationship (e.g., "
            "Strongly disagree < Disagree\n"
            "< Neutral < Agree).\n"
            "\n"
            "This field is intended to follow the ordering "
            "aspect of this [this pattern][this "
            "pattern](https://specs.frictionlessdata.io/patterns/#table-schema-enum-labels-and-ordering)\n",
            "title": "An ordered variable",
            "type": "boolean",
        },
        {
            "name": "missingValues",
            "description": "A list of missing values specific to a " "variable.\n",
            "title": "Missing Values",
            "examples": ["Missing|Skipped|No preference", "Missing"],
            "type": "string",
            "constraints": {"pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$"},
        },
        {
            "name": "trueValues",
            "description": "For boolean (true) variable (as defined in "
            "type field), this field allows\n"
            "a physical string representation to be cast as "
            "true (increasing\n"
            "readability of the field). It can include one "
            "or more values.\n",
            "title": "Boolean True Value Labels",
            "examples": ["required|Yes|Checked", "required"],
            "type": "string",
            "constraints": {"pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$"},
        },
        {
            "name": "falseValues",
            "description": "For boolean (false) variable (as defined in "
            "type field), this field allows\n"
            "a physical string representation to be cast as "
            "false (increasing\n"
            "readability of the field) that is not a "
            "standard false value. It can include one or "
            "more values.\n",
            "title": "Boolean False Value Labels",
            "examples": ["Not required|NOT REQUIRED", "No"],
            "type": "string",
            "constraints": {"pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$"},
        },
        {
            "name": "standardsMappings[0].instrument.url",
            "description": "A url (e.g., link, address) to a file or other "
            "resource containing the instrument, or\n"
            "a set of items which encompass a variable in "
            "this variable level metadata document (if at "
            "the root level or the document level) \n"
            "or the individual variable (if at the field "
            "level). \n",
            "title": "Url",
            "examples": [
                "https://www.heal.nih.gov/files/CDEs/2023-05/adult-demographics-cdes.xlsx"
            ],
            "type": "string",
        },
        {
            "name": "standardsMappings[0].instrument.source",
            "description": "An abbreviated name/acronym from a controlled "
            "vocabulary referencing the resource (e.g., "
            "program or repository)\n"
            "containing the instrument, or a set of items "
            "which encompass a variable in this variable "
            "level metadata document (if at the root level "
            "or the document level) \n"
            "or the individual variable (if at the field "
            "level). \n",
            "title": "Source",
            "type": "string",
            "constraints": {"enum": ["heal-cde"]},
        },
        {
            "name": "standardsMappings[0].instrument.title",
            "title": "Title",
            "examples": ["Adult demographics", "adult-demographics"],
            "type": "string",
        },
        {
            "name": "standardsMappings[0].instrument.id",
            "description": "A code or other string that identifies the "
            "instrument within the source.\n"
            "This should always be from the source's "
            "formal, standardized identification system \n",
            "title": "Identifier",
            "examples": ["5141"],
            "type": "string",
        },
        {
            "name": "standardsMappings[0].item.url",
            "description": "The url that links out to the published, "
            "standardized mapping of a variable (e.g., "
            "common data element)\n",
            "title": "Standards mappings - Url",
            "examples": [
                "https://evs.nci.nih.gov/ftp1/CDISC/SDTM/SDTM%20Terminology.html#CL.C74457.RACE"
            ],
            "type": "string",
        },
        {
            "name": "standardsMappings[0].item.source",
            "description": "The source of the standardized variable. Note, "
            "this property is required if \n"
            "an id is specified.\n",
            "title": "Standards mappings - Source",
            "examples": ["CDISC"],
            "type": "string",
        },
        {
            "name": "standardsMappings[0].item.id",
            "description": "The id locating the individual mapping within "
            "the given source. \n"
            "Note, the `standardsMappings[0].source` "
            "property is required if \n"
            "this property is specified.\n",
            "title": "Standards Mappings - Id",
            "examples": ["C74457"],
            "type": "string",
        },
    ],
    "missingValues": [""],
}
