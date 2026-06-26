const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.set("view engine", "ejs");
app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get("/", (req, res) => {
    res.render("index", { result: null });
});

app.post("/submit", (req, res) => {
    const { name, email } = req.body;
    console.log(`Received submission: Name - ${name}, Email - ${email}`);
    res.send("Form submitted successfully!");
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
