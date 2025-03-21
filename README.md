# uiform

<div align="center" style="margin-bottom: 1em;">

<img src="https://raw.githubusercontent.com/UiForm/uiform/refs/heads/main/uiform-logo.png" alt="UiForm Logo" width="150">


  *The AI Automation Platform*

Made with love by the team at [UiForm](https://uiform.com).

[Discord](https://discord.com/invite/vc5tWRPqag) | [Website](https://uiform.com) | [Twitter](https://x.com/uiformAPI)


</div>


``` bash
pip install uiform
```

First time here? Check our [docs](https://docs.uiform.com/get-started/introduction).

---

## How it works

UiForm allows you to easily create document processing automations. Here is the general workflow:

```mermaid
sequenceDiagram
    User ->> UiForm: File Upload
    UiForm -->> UiForm: Preprocessing
    UiForm ->> AI Provider: Request on your behalf
    AI Provider -->> UiForm:  Structured Generation
    UiForm ->> Webhook: Send result
    UiForm ->> User: Send Confirmation
```

---


We currently support [OpenAI](https://platform.openai.com/docs/overview) models.

You come with your own API key from your favorite AI provider, and we handle the rest.

---

UiForm solves three major challenges in document processing with LLMs:

1. **Universal Document Processing**: Convert any file type (PDFs, Excel, emails, etc.) into LLM-ready format without writing custom parsers
2. **Structured, Schema-driven Extraction**: Get consistent, reliable outputs using schema-based prompt engineering
3. **Automations**: Create custom mailboxes and links to process documents at scale

We see it as building **Stripe** for document processing.

Our goal is to make the process of analyzing documents and unstructured data as **easy** and **transparent** as possible.

Many people haven't yet realized how powerful LLMs have become at document processing tasks - we're here to help **unlock these capabilities**.


## Quickstart

### Setup of the Python SDK

To get started, install the `uiform` package using pip:

```bash
pip install uiform
```

Then, [create your API key on uiform.com](https://www.uiform.com) and populate your `env` variables with your API keys:

```
OPENAI_API_KEY=YOUR-API-KEY # Your AI provider API key. Compatible with OpenAI, Anthropic, xAI.
UIFORM_API_KEY=sk_xxxxxxxxx # Create your API key on https://www.uiform.com
```

### Summarize a document

Use the `UiForm` client to convert your documents into messages and use your favorite model to analyze your document:

```python 
from uiform import UiForm
from openai import OpenAI

uiclient = UiForm()
doc_msg = uiclient.documents.create_messages(
    document = "freight/booking_confirmation.jpg"
)

# Now you can use your favorite model to analyze your document
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=doc_msg.openai_messages + [
        {
            "role": "user",
            "content": "Summarize the document"
        }
    ]
)
```

---

### Load a schema and extract data from a document

We use a standard JSON Schema with custom annotations (`X-SystemPrompt`, `X-LLMDescription`, and `X-ReasoningDescription`) as a prompt-engineering framework for the extraction process.

These annotations help guide the LLM's behavior and improve extraction accuracy. 
You can learn more about these in our [JSON Schema documentation](https://docs.uiform.com/get-started/the-json-schema).


```python Pydantic BaseModel
from uiform import UiForm
from openai import OpenAI
from pydantic import BaseModel, Field, ConfigDict

uiclient = UiForm()
doc_msg = uiclient.documents.create_messages(
    document = "document_1.xlsx"
)

class CalendarEvent(BaseModel):
    model_config = ConfigDict(json_schema_extra = {"X-SystemPrompt": "You are a useful assistant."})

    name: str = Field(...,
        description="The name of the calendar event.",
        json_schema_extra={"X-LLMDescription": "Provide a descriptive and concise name for the event."}
    )
    date: str = Field(...,
        description="The date of the calendar event in ISO 8601 format.",
        json_schema_extra={
            'X-ReasoningDescription': 'The user can mention it in any format, like **next week** or **tomorrow**. Infer the right date format from the user input.',
        }
    )

print("Equivalent JSON Schema:",CalendarEvent.model_json_schema())

schema_obj =Schema(
    pydantic_model = CalendarEvent
)

# Now you can use your favorite model to analyze your document
client = OpenAI()
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=schema_obj.openai_messages + doc_msg.openai_messages,
    response_format=schema_obj.inference_pydantic_model
)
print("Extracted data with the reasoning fields:", completion.choices[0].message.content)

# Validate the response against the original schema if you want to remove the reasoning fields
assert completion.choices[0].message.content is not None
extraction = schema_obj.pydantic_model.model_validate_json(
    completion.choices[0].message.content 
)

print("Extracted data without the reasoning fields:", extraction)
```
</CodeGroup>

And that's it ! You can start processing documents at scale ! 
You have 1000 free requests to get started, and you can [subscribe](https://www.uiform.com) to the pro plan to get more.

But this minimalistic example is just the beginning. Continue reading to learn more about how to use UiForm **to its full potential**.

---

## Go further

- [Prompt Engineering Guide](https://docs.uiform.com/get-started/prompting-with-the-json-schema)
- [General Concepts](https://docs.uiform.com/get-started/General-Concepts)
- [Create mailboxes](https://docs.uiform.com/SDK/Automations#mailbox)
- [Create links](https://docs.uiform.com/SDK/Automations#link)
- Finetuning (coming soon)
- Prompt optimization (coming soon)
- Data-Labelling with our AI-powered annotator (coming soon)

---

## Jupyter Notebooks

You can view minimal notebooks that demonstrate how to use UiForm to process documents:
- [Mailbox creation quickstart](https://github.com/UiForm/uiform/blob/main/notebooks/mailboxes_quickstart.ipynb)
- [Upload Links creation quickstart](https://github.com/UiForm/uiform/blob/main/notebooks/links_quickstart.ipynb)
- [Document Extractions quickstart](https://github.com/UiForm/uiform/blob/main/notebooks/Quickstart.ipynb)
- [Document Extractions quickstart - Async](https://github.com/UiForm/uiform/blob/main/notebooks/Quickstart-Async.ipynb)

--- 

## Community

Let's create the future of document processing together!

Join our [discord community](https://discord.com/invite/vc5tWRPqag) to share tips, discuss best practices, and showcase what you build. Or just [tweet](https://x.com/uiformAPI) at us.

We can't wait to see how you'll use UiForm.

- [Discord](https://discord.com/invite/vc5tWRPqag)
- [Twitter](https://x.com/uiformAPI)


## Roadmap

We publicly share our Roadmap with the community. Please open an issue or [contact us on X](https://x.com/sachaicb) if you have suggestions or ideas.

- [ ] node client with ZOD
- [ ] Make a json-schema zoo
- [ ] Offer tools to display tokens usage to our users
- [ ] Launch the data-labelling API (Dataset Upload / Creation / Management / Labelling / Distillation)
- [ ] Launch the data-labelling platform : A web app based on the data-labelling API with a nice UI
- [ ] Launch the prompt-optimisation sdk
- [ ] Launch the finetuning sdk 
