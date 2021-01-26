
////
//
// Course Actions
//
////

import * as CourseAPIUtilities from '../utilities/course_api_utilities';

////
// Action Types
////

export const RECEIVE_COURSES = 'RECEIVE_COURSES';
export const RECEIVE_COURSE = 'RECEIVE_COURSE';
export const REMOVE_COURSE = "REMOVE_COURSE";


////
// Regular action creators which return objects
////

// Accepts courses
export const receiveCourses = courses => ({
  type: RECEIVE_COURSES,
  payload: courses,
})

// Accept a course
export const receiveCourse = ({ course }) => ({
  type: RECEIVE_COURSE,
  payload: course
});

// Accept a course
export const removeCourse = ({ course }) => ({
  type: REMOVE_COURSE,
  payload: course
});


////
// Thunk async action creators which return functions
////

//
export const fetchCourses = () => dispatch => (
  CourseAPIUtilities.fetchCourses().then(courses => (
    dispatch(receiveCourses(courses))
  ))
);

//
export const fetchCourse = id => dispatch => (
  CourseAPIUtilities.fetchCourse(id).then(course => (
    dispatch(receiveCourse(course))
  ))
);

//
export const createCourse = course => dispatch => (
  CourseAPIUtilities.createCourse(course).then(course => (
    dispatch(receiveCourse(course))
  ))
);

//
export const updateCourse = course => dispatch => (
  CourseAPIUtilities.updateCourse(course).then(course => (
    dispatch(receiveCourse(course))
  ))
);

//
export const deleteCourse = course => dispatch => (
  CourseAPIUtilities.destroyCourse(course).then(course => (
    dispatch(removeCourse(course))
  ))
);
