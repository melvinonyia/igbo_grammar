
////
//
// Course List - Presentation Component
//
////

import React from 'react';
import { Link } from 'react-router-dom';
import CourseDetail from './course_detail';

const CourseShow = ({ course, courseId, fetchCourse }) => {
  const courses = {
    [courseId]: course
  };

  return(
    <div className="single-course-show">
      <div className="right-half course-details">
        <CourseDetail course={course} />
      </div>
    </div>
  );
};

export default CourseShow;
