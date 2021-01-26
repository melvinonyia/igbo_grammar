
////
//
// Deck API Utilities
//
////

// Deck index API
export const fetchDecks = data => (
  $.ajax({
    method: 'GET',
    url: '/api/decks',
    data
  })
);

// Show individual deck API
export const fetchDeck = id => (
  $.ajax({
    method: 'GET',
    url: '/api/decks/${id}'
  })
);

// Create deck API
export const createDeck = deckForm => (
  $.ajax({
    method: 'POST',
    url: '/api/decks',
    data: deckForm,
    contentType: false,
    processData: false
  })
);

// Edit deck API
export const editDeck = deckForm => (
  $.ajax({
    method: 'PATCH',
    url: '/api/decks/${id}',
    data: deckForm,
    contentType: false,
    processData: false
  })
);

// Delete deck API
export const deleteDeck = () => (
  $.ajax({
    method: 'DELETE',
    url: '/api/decks/${id}'
  })
);
