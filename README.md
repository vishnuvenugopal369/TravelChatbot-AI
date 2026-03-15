# AI Travel Chatbot ✈️

This project demonstrates a simple **AI-powered travel assistant** that understands travel requests written in natural language.

The chatbot extracts travel information such as:

* Origin city
* Destination city
* Travel date

and returns possible flight options.

## Example Query

User input:

```
Find flights from Berlin to Paris tomorrow
```

Parsed output:

```
Origin: Berlin
Destination: Paris
Date: Tomorrow
```

Example flight results:

```
Lufthansa 08:30
Ryanair 12:15
EasyJet 18:45
```

## Technologies Used

* Python
* spaCy (Natural Language Processing)
* dateparser

## Project Structure

```
TravelChatbot-AI
│
├── app.py
├── nlp_parser.py
├── flight_search.py
├── requirements.txt
└── README.md
```

## How It Works

1. User enters a travel request.
2. NLP parser extracts cities and dates.
3. The system searches available flights.
4. The chatbot returns flight options.

## Future Improvements

* Connect to real flight APIs
* Add a web interface
* Integrate LLM-based conversations

---

MSc Artificial Intelligence Student
