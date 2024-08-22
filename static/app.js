const $userInput = $('#guess')

async function sendGuess(e) {
    e.preventDefault();
    let guess = $userInput.val();
    $userInput.val(''); //clear search bar
    const res = await axios.get('http://127.0.0.1:5000/guess', { //
        params: { guess },
        headers: {
            'Accept': 'application/json'
        }
    })
    console.log(res.data);
}

$('#submit').on('click', sendGuess);

// const res = await axios.post('http://127.0.0.1:5000/guess', new URLSearchParams({ guess: guess }));
