import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <style>
                body {
                    text-align: center;
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                }
                img {
                    display: block;
                    margin: 20px auto;
                }
                p {
                    text-align: justify;
                    margin: 20px 50px;
                    font-size: 16px;
                    line-height: 1.6;
                    color: #333;
                }
                .info-section {
                    margin: 20px 0;
                    padding: 10px;
                    background-color: #ffffff;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                button {
                    padding: 10px 20px;
                    font-size: 16px;
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    margin-top: 20px;
                }
                button:hover {
                    background-color: #0056b3;
                }
                h1 {
                    color: #004085;
                }
            </style>
            <script>
                function toggleInfo() {
                    var infoText = document.getElementById("extraInfo");
                    if (infoText.style.display === "none") {
                        infoText.style.display = "block";
                    } else {
                        infoText.style.display = "none";
                    }
                }
            </script>
        </head>
        <body>
            <h1>Welcome to Malnad College of Engineering</h1>
            <img src="https://careermudhra.com/wp-content/uploads/malnad-college-of-engineering-hassan-jpg.webp" alt="Malnad College Entrance" width="500">
            
            <p>Malnad College of Engineering, An Autonomous Institution, Affiliated by VTU, established in the year 1960, during the second 5-year plan, as a joint venture o
f Government of India, Government of Karnataka, and the Malnad Technical Education Society, Hassan. The Malnad College of Engineering is now a reputed Engineering college in
 the country. The college has earned the “ISTE Award” as one of the Best Engineering Colleges in the Country, in the year 2007.</p>

            <div class="info-section">
                <p id="extraInfo" style="display:none;">
                    The Institute is located in the midway, (13°N and 76.5°E, altitude 943 mtrs.) between Bengaluru (180 kms) and Mangaluru (170 kms) on NH-75. Hassan, a dis
trict headquarter, has a steady temperate climate throughout the year and enjoys an annual rainfall of about 900 mm. World-famous temples of Belur, Halebidu, Shravanabelagol
a, and The Master Control Facility for INSAT Satellites are located in Hassan District.
                    <br><br>
                    The College is built on a 41.28-acre campus and has all the facilities expected in a modern Engineering College. The college offers 9 B.E, 5 M.Tech, M.Sc
.(Engg.) by Research, Ph.D., and MCA programs, with about 4000 students enrolled. The college is one of the few Engineering Colleges in the country recognized for conducting
 the Technical Education Quality Improvement Programme (TEQIP) sponsored by the World Bank. 
                    <br><br>
                    The Training and Placement center in the college trains and assists the students in securing employment in reputed companies like Tata Consultancy, Infos
ys, Wipro, L&T, BEL, Fistchner, Builders’ Association of India, etc., through campus recruitment programs.
                </p>
                <button onclick="toggleInfo()">Click to Learn More</button>
            </div>
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)