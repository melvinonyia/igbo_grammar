
////
//
// Deck List Item - Presentation Component
//
////

import React from 'react';

const DeckListItem = ({ item }) => (
	<div className="deck-list-item">
		<h3>{item.name}</h3>
		<span>{item.objective}</span>
	</div>
);

export default DeckListItem;
