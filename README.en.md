# Melodic Search with Elasticsearch

🎶 **Fuzzy search for melodic patterns using contours and n-grams in Elasticsearch**

This project demonstrates how to adapt text search mechanisms to find **similar melodic patterns**, even with transpositions or small variations. The approach combines musical abstraction, symbolic NLP, and the power of Elasticsearch.

---

## 🔍 Overview

The idea was born from the following question:

> What if it was possible to search for melodies the same way we search for sentences with typos?

In this repository, you will find:
- Transformation of melodies into symbolic contours (`U-Up`, `D-Down`, `R-Repeat`)
- Generation of n-grams from these contours
- Mapping and analysis in Elasticsearch with `fuzziness` support
- Query examples and result visualizations

---

## 🧠 Motivation

This work was inspired by and expanded from my master's thesis, where I explore the symbolic representation of melodies in more depth:

🔗 [My LinkedIn (thesis attached in Academic Background)](https://www.linkedin.com/in/alexcaranha/)

---

## 🚀 How to run

You can easily run the project using Docker Compose:

```sh
docker-compose up
```

This will start both Elasticsearch and the melodic search service.

📊 Demonstration

Using the excerpt from the song "Happy Birthday" below, without the note E (highlighted in blue):
<img src="assets/happy_birthday_selection.png" alt="Demo">

We provide the program with the pattern "RUDDD", highlighted in the green box in the image above, to search for songs in the database (composed of 10 songs).

The system correctly finds the song "Happy Birthday".
<img src="assets/demonstration.gif" alt="Demo">