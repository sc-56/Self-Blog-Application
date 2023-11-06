function handle_1() {
    
    // submit_button.textContent = "hi";
    note.innerHTML += 'Extra stuff';
    
};

const submit_button = document.getElementById("submit-button");
const note = document.getElementById("note");
const text_area = document.getElementById("text-area");

submit_button.addEventListener('click', handle_1, false);