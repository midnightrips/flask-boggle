const $userInput = $('#guess')

async function sendGuess(e) {
    e.preventDefault();
    let guess = $userInput.val();
    $userInput.val(''); //clear search bar
    const res = await axios.get('http://localhost', { params: { guess } })
    console.log(res);
}

$('#submit').on('click', sendGuess);