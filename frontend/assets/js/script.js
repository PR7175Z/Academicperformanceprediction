document.addEventListener('DOMContentLoaded', ()=>{
    const resultDisplay = document.getElementById('result');

    //API fetching function
    async function get_response(ParentalSupport, PreviousGrade, StudyHoursPerWeek, ExtracurricularActivities, AttendanceRate) {
        const features = {'features': [ParentalSupport, PreviousGrade, StudyHoursPerWeek, ExtracurricularActivities, AttendanceRate ]};

        const api = 'http://127.0.0.1:8000/predict';
        const response = await fetch(api,{
                method : 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify(features)
            }
        )

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        return data;
    }

    //eventlisterner for form submission
    document.getElementById('inputform').addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.querySelector('input[name="name"]').value;
        const gender = document.querySelector('input[name="gender"]').value;
        const attendance = document.querySelector('input[name="attendance"]').value;
        const studyHour = document.querySelector('input[name="studyhour"]').value;
        const previousGrade = document.querySelector('input[name="previousgrade"]').value;
        const extraCurricularActivities = document.querySelector('input[name="extracurricularactivities"]').value;
        const parentalSupport = document.querySelector('select[name="parentalsupport"]').value;


        //asynchronous function for response
        async function displayResponse() {
            try {
                const heading = document.createElement('h3');
                const prediction = document.createElement('p');
                heading.innerHTML = `Hello ${name}`;
                const response = await get_response( parseInt(parentalSupport), previousGrade, studyHour, extraCurricularActivities, attendance);

                prediction.innerHTML = response
                resultDisplay.appendChild(heading);
                resultDisplay.appendChild(prediction);
            } catch (error) {
                console.error("Error:", error);
            }
        }

        displayResponse();
    })
})