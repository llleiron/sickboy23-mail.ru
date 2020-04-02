function sendJSON(){ 
    let hinvadacele = document.querySelector('#ՀիվանդացելԷ'); 
    let viravorumnery = document.querySelector('#վիրավորումները'); 
    let kontuzianery = document.querySelector('#Կոնտուզիաները');
    let virahatutyunnery = document.querySelector('#Վիրահատությունները');
    let ardzakurdnery = document.querySelector('#ԱրձակուրդներըՀիվանդությանՊատճառով');
    let bujumn = document.querySelector('#ԲուժումնԱռողջարաններում');
    let jarangakanutyun = document.querySelector('#Ժառանգականությունը');
    let inchdexer = document.querySelector('#ԻնչԴեղերՉիԿարողանումԸնդունել');
    let nerarkumner = document.querySelector('#ՆերարկումներիԱզդեցությունը');
    let vnasakar = document.querySelector('#ՎնասակարՍովորությունները');
    let hatuknshumner = document.querySelector('#ՀատուկՆշումներ');
    let hh = document.querySelector('#հհ')
    // Creating a XHR object 
    let a = new XMLHttpRequest(); 
    const b = "http://127.0.0.1:8000/Anamnez/create"; 
    // open a connection 
    a.open("POST", b, true); 
    // Set the request header i.e. which type of content you are sending 
    a.setRequestHeader("Content-Type", "application/json"); 
    // Create a state change callback 
    a.onreadystatechange = function () { 
        if (a.readyState === 4 && a.status === 200) { 
            // Print received data from server 
            result.innerHTML = this.responseText; 
        } 
    }; 
    // Converting JSON data to string 
    var dita = JSON.stringify({
        "հհ": hh.value,
        "վիրավորումները": viravorumnery.value,
        "ՀիվանդացելԷ": hinvadacele.value,
        "Կոնտուզիաները": kontuzianery.value,
        "Վիրահատությունները": virahatutyunnery.value,
        "ԱրձակուրդներըՀիվանդությանՊատճառով": ardzakurdnery.value,
        "ԲուժումնԱռողջարաններում": bujumn.value,
        "Ժառանգականությունը": jarangakanutyun.value,
        "ԻնչԴեղերՉիԿարողանումԸնդունել": inchdexer.value,
        "ՆերարկումներիԱզդեցությունը": nerarkumner.value,
        "ՎնասակարՍովորությունները": vnasakar.value,
        "ՀատուկՆշումներ": hatuknshumner.value,

        }); 

    // Sending data with the request 
    
    a.send(dita);
    
        window.location.assign('../../Grancum/HTML/registraion.html')

     }
     