const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

const axios = require("axios");

const BACKEND_URL = "http://100.24.58.12:5000/";

app.set("view engine", "ejs");
app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get("/", (req, res) => {
    res.render("index", { result: null });
});

app.post("/submit", async (req, res) => {
    const { name, email } = req.body;

    try {
        const response = await axios.post(`${BACKEND_URL}/process`, {
            name,
            email
        });

        res.send(response.data);

    } catch (error) {
        res.status(500).send("Backend not reachable");
    }
});

app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server is running on port ${PORT}`);
});