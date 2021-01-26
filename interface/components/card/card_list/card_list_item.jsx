
////
//
// Card List Item - Presentation Component
//
////

import React from 'react';

const CardListItem = ({ item }) => (
	<div className="card-list-item">
		<span>{item.question}</span>
		<span>{item.answer}</span>
	</div>
);

export default CardListItem;
