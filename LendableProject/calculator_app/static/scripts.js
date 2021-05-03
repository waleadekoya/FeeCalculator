const term = document.getElementById("term");
const fees = document.getElementById("fees");

term.onchange = () => {
    let value = term.value;

    fetch("/fees/" + value).then(result => {
        result.json().then(data => {
            let optionHtml = '';
            console.log(data["fees"])
            for (let option of data["fees"]) {
                optionHtml += `<option value ="${option}">${option}</option>`;
            }
            fees.innerHTML = optionHtml;
        });
    });

}