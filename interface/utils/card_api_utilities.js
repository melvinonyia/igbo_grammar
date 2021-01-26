
////
//
// Card API Utilities
//
////

// Cards index API
export const fetchCards = data => (
  $.ajax({
    method: 'GET',
    url: '/api/cards',
    data
  })
);

// Show individual card API
export const fetchCard = id => (
  $.ajax({
    method: 'GET',
    url: '/api/cards/${id}'
  })
);

// Create card API
export const createCard = cardForm => (
  $.ajax({
    method: 'POST',
    url: '/api/cards',
    data: cardForm,
    contentType: false,
    processData: false
  })
);

// Edit card API
export const editCard = cardForm => (
  $.ajax({
    method: 'PATCH',
    url: '/api/cards/${id}',
    data: cardForm,
    contentType: false,
    processData: false
  })
);

// Delete card API
export const deleteCard = () => (
  $.ajax({
    method: 'DELETE',
    url: '/api/cards/${id}'
  })
);
