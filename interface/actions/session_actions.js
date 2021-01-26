
////
//
// Session Actions
//
////

import * as APIUtilities from '../utilities/session_api_utilities';

////
// Action Types
////

export const RECEIVE_CURRENT_USER = 'RECEIVE_CURRENT_USER';
export const LOGOUT_CURRENT_USER = 'LOGOUT_CURRENT_USER';
export const RECEIVE_SESSION_ERRORS = 'RECEIVE_SESSION_ERRORS';


////
// Regular action creators
////

// accept a user object
export const receiveCurrentUser = currentUser => ({
  type: RECEIVE_CURRENT_USER,
  currentUser
});

// accept no argument
export const logoutCurrentUser = () => ({
  type: LOGOUT_CURRENT_USER,
});

// take an array
export const receiveErrors = errors => ({
  type: RECEIVE_SESSION_ERRORS,
  errors
});


////
// Thunk action creators
////

// Signup actioncreators, accept a user object
export const signup = user => dispatch => (
  APIUtilities.signup(user).then(user => (
    dispatch(receiveCurrentUser(user))
  ), err => (
    dispatch(receiveErrors(err.responseJSON))
  ))
);

// Login action creators, accept a user object
export const login = user => dispatch => (
  APIUtilities.login(user).then(user => (
    dispatch(receiveCurrentUser(user))
  ), err => (
    dispatch(receiveErrors(err.responseJSON))
  ))
);

// Logout action, accepts no argument
export const logout = () => dispatch => (
  APIUtilities.logout().then(user => (
    dispatch(logoutCurrentUser())
  ))
);
