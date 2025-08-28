error_responses = {
    400: {
        "description": "Invalid character description",
        "content": {"application/json": {"example": {"detail": "Please describe a character with a name, traits, and a conflict"}}},
    },
    401: {
        "description": "Authentication error with OpenAI/OpenRouter",
        "content": {"application/json": {"example": {"detail": "Invalid or missing API key"}}},
    },
    422: {
        "description": "Validation error (invalid request body)",
        "content": {"application/json": {"example": {"detail": [{"loc": ["body", "description"], "msg": "field required", "type": "value_error.missing"}]}}},
    },
    429: {
        "description": "Too many requests / quota exceeded",
        "content": {"application/json": {"example": {"detail": "You exceeded your current quota"}}},
    },
    503: {
        "description": "Service unavailable (network issues, upstream unavailable)",
        "content": {"application/json": {"example": {"detail": "OpenAI service temporarily unavailable"}}},
    },
    500: {
        "description": "Unexpected internal error",
        "content": {"application/json": {"example": {"detail": "Unexpected internal error"}}},
    },
}
