
////
//
// Course List Item - Presentation Component
//
////

import React from 'react';

const CourseListItem = ({ course }) => {
	return(
		<li className="course-list-item">
			<h3 className='course-item-name'>{course.name}</h3>
			<span className='course-item-description'>{course.description}</span>
		</li>
	);
}

export default CourseListItem;
