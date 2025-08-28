error_responses = {
    400: {
        "description": "Invalid character description",
        "content": {
            "application/json": {
                "example": {"detail": "Please describe a character with a name, traits, and a conflict."}
            }
        },
    },
    422: {
        "description": "Validation error (invalid request body)",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": ["body", "description"],
                            "msg": "field required",
                            "type": "value_error.missing",
                        }
                    ]
                }
            },
        },
    },
    500: {
        "description": "Internal error (e.g., OpenAI quota exceeded)",
        "content": {
            "application/json": {
                "example": {"detail": "OpenAI quota exceeded"}
            }
        },
    },
}
