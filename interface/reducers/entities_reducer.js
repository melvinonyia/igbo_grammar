
////
//
// Entities Reducer
//
////

import { combineReducers } from 'redux';

import users from './users_reducer';
import courses from './courses_reducer';
//import decks from './decks_reducer';
//import cards from './cards_reducer';

export default combineReducers({
  users,
  courses,
  //decks,
  //cards,
});
