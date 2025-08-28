# 📖 Character Stories API

This project is a RESTful API that generates **deep and psychologically coherent stories** for fictional characters.  
It uses **LangChain + LangGraph** to orchestrate a multi-step reasoning pipeline:

1. **Validation** – Checks if the input is a proper character description.  
2. **Classification** – Identifies the most suitable **Enneagram type (1–9)**.  
3. **Story Generation** – Creates a detailed narrative consistent with the character’s Enneagram type.

---

## 🔬 How It Works

The pipeline is powered by an LLM (via **OpenRouter/OpenAI**) and structured as a **graph**:

- **Validation node** → ensures the user input includes a name/role, traits, and a conflict.  
- **Classification node** → selects one of the nine Enneagram types and enriches it with a fixed explanation.  
- **Story node** → generates a psychologically consistent story, including childhood, fears, motivations, and relationships.  

If validation fails, the API responds with **400 Bad Request**.  

---

## 📚 Swagger Documentation

Interactive API documentation is automatically generated via **Swagger UI** and available at:

```
/docs
```

### Example request:

```json
{
  "description": "Michael, a brave knight who struggles to connect with people"
}
```

### Example response:

```json
{
  "eneatype_number": "4",
  "character_story": "Michael, identified as an Individualist knight, grew up feeling different..."
}
```

If the request does not describe a valid character:

```json
{
  "detail": "Please describe a character with a name, traits, and a conflict."
}
```

---

## ⚙️ Setup Instructions

1. **Install the dependencies in a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate    # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. **Create your environment file**:

Copy the `.env.example` to `.env` and provide the values:

```env
OPENAI_API_KEY=your-api-key
OPENAI_API_BASE=https://openrouter.ai/api/v1
MODEL_NAME=mistralai/mistral-7b-instruct:free
```

3. **Run the development server**:

```bash
uvicorn app.main:app --reload
```

Access the application in your browser at:

```
http://127.0.0.1:8000/docs
```

---

## 📜 License

This project is released under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it — with attribution.  

---

## 👤 Author

Developed by [Francisco Jesús Montero Martínez](https://github.com/framonmar7)  
For suggestions, improvements, or collaboration, feel free to reach out.  
