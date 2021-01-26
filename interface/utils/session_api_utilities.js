
////
//
// Session API Utilities
//
////

// Login API
export const login = user => (
  $.ajax({
    method: 'POST',
    url: '/api/session',
    data: { user }
  })
);

// Signup API
export const signup = user => (
  $.ajax({
    method: 'POST',
    url: '/api/user',
    data: { user }
  })
);

// Logout API
export const logout = () => (
  $.ajax({
    method: 'DELETE',
    url: '/api/session'
  })
);
