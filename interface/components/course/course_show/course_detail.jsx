
////
//
// Course Detail - Presentation Component
//
////

import React from 'react';
import { Link } from 'react-router';

// import DeckListItemContainer from './deck_list_item_container';

//const deckList = (decks) => (
//  decks.map(deck => (
//    <DeckListItemContainer
//      deck={deck}
//      key={deck.id}
//    />
//  ))
//);

const CourseDetail = ({ course }) => {
  return (
    <div>
      <ul className="course-list">
        <li>Name: {course.name}</li>
        <li>Description: {course.description}</li>
      </ul>
      <br/>
      //<div className="decks">
      //  <h3>Decks</h3>
      //  {deckList(decks)}
      //</div>
    </div>
  );
};

export default CourseDetail;
