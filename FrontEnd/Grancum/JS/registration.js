function sendJSON(){ 
    let name = document.querySelector('#Անուն'); 
    let surname = document.querySelector('#Ազգանուն'); 
    let fathername = document.querySelector('#Հայրանուն');

    // Creating a XHR object 
    let xhr = new XMLHttpRequest(); 
    const url = "http://127.0.0.1:8000/Grancum/create"; 
    // open a connection 
    xhr.open("POST", url, true); 
    // Set the request header i.e. which type of content you are sending 
    xhr.setRequestHeader("Content-Type", "application/json"); 
    // Create a state change callback 
    xhr.onreadystatechange = function () { 
        if (xhr.readyState === 4 && xhr.status === 200) { 
            // Print received data from server 
            result.innerHTML = this.responseText; 
        } 
    }; 
    // Converting JSON data to string 
    var data = JSON.stringify({
        "Ազգանուն": surname.value,
        "Անուն": name.value,
        "Հայրանուն": fathername.value,
        }); 

    // Sending data with the request 
    
    xhr.send(data);
    
       window.location.assign('../../Anamnez/HTML/anamnez.html')

     }
     