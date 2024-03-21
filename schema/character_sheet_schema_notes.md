# Character Sheet JSON Schema Segments

## Inventory
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "D&D Inventory and Equipment",
  "type": "object",
  "properties": {
    "character_id": {"type": "string"},
    "equipped": {
      "type": "object",
      "properties": {
        "head": {"$ref": "#/definitions/item"},
        "neck": {"$ref": "#/definitions/item"},
        "body": {"$ref": "#/definitions/item"},
        "armor": {"$ref": "#/definitions/item"},
        "main_hand": {"$ref": "#/definitions/item"},
        "off_hand": {"$ref": "#/definitions/item"},
        "feet": {"$ref": "#/definitions/item"},
        "rings": {
          "type": "array",
          "items": {"$ref": "#/definitions/item"},
          "maxItems": 2
        },
        "cloak": {"$ref": "#/definitions/item"},
        "belt": {"$ref": "#/definitions/item"},
        "gloves": {"$ref": "#/definitions/item"},
        "worn_miscellaneous": {
          "type": "array",
          "items": {"$ref": "#/definitions/item"}
        }
      }
    },
    "carried": {
      "type": "array",
      "items": {"$ref": "#/definitions/item"}
    },
    "gold": {"type": "number"}
  },
  "definitions": {
    "item": {
      "type": "object",
      "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "type": {"type": "string"},
        "subtype": {"type": "string"},
        "weight": {"type": "number"},
        "properties": {
          "type": "object",
          "properties": {
            // Refer back to the detailed properties as defined in the D&D Item schema.
          }
        },
        "contents": {
          "type": "array",
          "items": {"$ref": "#/definitions/item"},
          "description": "For containers, this array holds items contained within."
        }
      },
      "required": ["id", "name", "type", "weight"]
    }
  },
  "required": ["character_id", "equipped", "carried", "gold"]
}

## Items

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "D&D Item",
    "type": "object",
    "properties": {
      "id": {"type": "string"},
      "name": {"type": "string"},
      "description": {"type": "string"},
      "type": {"type": "string"},
      "subtype": {"type": "string", "enum": ["container", "wearable", "weapon", "consumable", "tool", "magical", "artifact", "miscellaneous"]},
      "weight": {"type": "number"},
      "value": {"type": "string"},
      "properties": {
        "type": "object",
        "properties": {
          "magical": {"type": "boolean"},
          "requires_attunement": {"type": "boolean"},
          "charges": {"type": "integer"},
          "effects": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "effect": {"type": "string"},
                "description": {"type": "string"},
                "duration": {"type": "string"},
                "charges_used": {"type": "integer"}
              },
              "required": ["effect"]
            }
          },
          "consumable": {"type": "boolean"},
          "activation": {
            "type": "object",
            "properties": {
              "command": {"type": "string"},
              "action_type": {"type": "string"}
            }
          },
          "restrictions": {
            "type": "array",
            "items": {"type": "string"}
          },
          "armor_class": {"type": "integer"},
          "damage": {
            "type": "object",
            "properties": {
              "dice_count": {"type": "integer"},
              "dice_value": {"type": "integer"},
              "damage_type": {"type": "string"}
            }
          },
          "capacity": {
            "type": "object",
            "properties": {
              "unit": {"type": "string"},
              "amount": {"type": "number"}
            }
          },
          "wear_slot": {"type": "string"},
          "proficiencies": {
            "type": "array",
            "items": {"type": "string"}
          },
          "special_features": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "feature": {"type": "string"},
                "description": {"type": "string"}
              }
            }
          }
        }
      }
    },
    "required": ["id", "name", "type", "weight", "value", "properties"]
  }

## Wearables

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "D&D Wearables",
    "type": "object",
    "properties": {
      "name": {"type": "string"},
      "type": {"type": "string"},
      "description": {"type": "string"},
      "magical": {"type": "boolean"},
      "requires_attunement": {"type": "boolean"},
      "equipped": {
        "type": "boolean",
        "description": "Indicates if the item is currently equipped."
      },
      "attuned": {
        "type": ["boolean", "null"],
        "description": "Indicates if the item is attuned (null if attunement not required)."
      },
      "weight": {
        "type": "number",
        "description": "The weight of the item in pounds."
      },
      "armor_class": {
        "type": ["integer", "null"],
        "description": "The armor class provided by the item, if applicable."
      },
      "enhancement_bonus": {
        "type": ["integer", "null"],
        "description": "Bonus to armor class or other statistics for magical items."
      },
      "wear_slot": {
        "type": "string",
        "description": "The body slot the item occupies (e.g., head, body, feet)."
      },
      "compatible_with": {
        "type": "array",
        "items": {"type": "string"},
        "description": "List of other types of clothing that can be worn together with this item."
      },
      "restrictions": {
        "type": "object",
        "properties": {
          "character_types": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Character types that cannot wear the item."
          },
          "materials": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Materials that the item cannot be made of, if applicable."
          }
        }
      },
      "proficiencies": {
        "type": "array",
        "items": {"type": "string"},
        "description": "List of specific proficiencies required to use the item effectively."
      },
      "effects": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "effect": {"type": "string"},
            "description": {"type": "string"}
          },
          "required": ["effect", "description"]
        },
        "description": "The effects provided by wearing the item, if any."
      },
      "special_features": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "feature": {"type": "string"},
            "description": {"type": "string"}
          },
          "required": ["feature", "description"]
        },
        "description": "Special features or functionalities of the item."
      }
    },
    "required": ["name", "type", "wear_slot", "equipped", "weight"]
  }

  ## Containers

  {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "D&D Container",
    "type": "object",
    "properties": {
      "name": {"type": "string"},
      "type": {"type": "string"},
      "description": {"type": "string"},
      "weight": {"type": "number"},
      "capacity": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "weight": {"type": "number"},
              "volume": {"type": "number"}
            },
            "required": [],
            "additionalProperties": false
          },
          {
            "type": "number"
          }
        ]
      },
      "contents": {
        "type": "array",
        "items": {
          "$ref": "#"
        }
      },
      "magical": {"type": "boolean", "default": false},
      "requires_attunement": {"type": "boolean", "default": false},
      "attuned": {"type": ["boolean", "null"], "default": null},
      "equipped": {"type": "boolean", "default": false},
      "wear_slot": {
        "type": ["string", "null"],
        "description": "Optional slot indicating where the container is worn."
      },
      "magical_properties": {
        "type": "object",
        "properties": {
          "effects": {
            "type": "array",
            "items": {"type": "string"}
          },
          "charges": {"type": "integer", "minimum": 0},
          "activation_word": {"type": "string"}
        }
      },
      "restrictions": {
        "type": "array",
        "items": {"type": "string"}
      },
      "special_features": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "feature": {"type": "string"},
            "description": {"type": "string"}
          },
          "required": ["feature", "description"]
        }
      }
    },
    "required": ["name", "type", "weight", "capacity"]
  }
  
  ## Weapons
  {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "D&D Weapon",
    "type": "object",
    "properties": {
      "name": {"type": "string"},
      "description": {"type": "string"},
      "notes": {"type": "string", "default": ""},
      "type": {"type": "string"},
      "attackType": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": ["melee", "ranged", "both"]
        },
        "minItems": 1,
        "uniqueItems": true,
        "description": "Indicates the attack types the weapon is designed for."
      },
      "damage": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "dice_string": {"type": "string"},
            "damage_type": {"type": "string"},
            "modifier": {"type": "string", "default": "None"},
            "condition": {
              "type": "string",
              "description": "Describes under what condition or attack type this damage applies."
            }
          },
          "required": ["dice_string", "damage_type"]
        },
        "description": "Details of damage the weapon deals, which can vary based on attack type."
      },
      "weight": {"type": "number"},
      "properties": {
        "type": "array",
        "items": {"type": "string"}
      },
      "magical": {"type": "boolean", "default": false},
      "requires_attunement": {"type": "boolean", "default": false},
      "attuned": {"type": "boolean", "default": false},
      "equipped": {"type": "boolean", "default": false},
      "slot": {
        "type": "string",
        "enum": ["mainhand", "offhand", "two-handed", "not applicable"],
        "default": "not applicable"
      },
      "range": {
        "type": "object",
        "properties": {
          "normal": {"type": "integer"},
          "maximum": {"type": "integer"}
        },
        "required": ["normal"],
        "description": "Specifies the range for ranged attack types; required if 'ranged' is included in attackType."
      },
      "reach": {
        "type": "integer",
        "default": 5,
        "description": "Specifies the reach for melee attack types; relevant if 'melee' is included in attackType."
      },
      "ammunition": {
        "type": "object",
        "properties": {
          "type": {"type": "string"},
          "quantityUsed": {"type": "integer", "minimum": 0, "default": 1},
        },
        "required": ["type"]
      },
      "enhancement_bonus": {"type": "integer", "default": 0}
    },
    "required": ["name", "type", "damage", "weight", "attackType"]
  }

 ## NPC Character Summaries

 {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Character Summary",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "relationship": {
      "type": "string"
    },
    "race": {
      "type": "string",
      "optional": true
    },
    "age": {
      "type": "integer",
      "optional": true
    },
    "status": {
      "type": "string",
      "enum": ["Alive", "Deceased"]
    },
    "profession": {
      "type": "string",
      "optional": true
    },
    "factions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "personality": {
      "type": "string",
      "optional": true
    },
    "backstory": {
      "type": "string",
      "optional": true
    },
    "appearance": {
      "type": "string",
      "optional": true
    },
    "pronouns": {
      "type": "string"
    },
    "location": {
      "type": "string",
      "optional": true
    },
    "home": {
      "type": "string",
      "optional": true
    },
    "current_location": {
      "type": "string",
      "optional": true
    }
  },
  "required": [
    "name",
    "relationship",
    "status",
    "factions",
    "pronouns"
  ]
}
 