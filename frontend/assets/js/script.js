document.addEventListener('DOMContentLoaded', ()=>{
    async function get_response() {
        const features = {'features': [0, 20, 10, 3, 51.6587823 ]};

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
    }

    get_response();
})