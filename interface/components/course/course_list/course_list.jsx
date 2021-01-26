
////
//
// Course List Component
//
////

import React from 'react';
import { useSelector } from 'react-redux';
// Bring in the asynchronous fetchPosts action
import { fetchCourses } from '../../../actions/course_actions';
import CourseListItem from './course_list_item';

const CourseList = () => {

	// const somePieceOfData = useSelector( state => state.path.to.data )
	const courses = useSelector( state => state.courses )

	return(
		<div className="course-list">
			<h3>Courses</h3>
			<ul className='course-list-items'>
				{courses.map(course => (
						<CourseListItem key={course.id} course={course} />
					))}
			</ul>
		</div>
	);
}

export default CourseList;
