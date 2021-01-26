
////
//
// Class List Presentation Component
//
////

import { connect } from 'react-redux';
import { fetchCourse } from '../../../actions/course_actions';
import CourseShow from './course_show';

const mapStateToProps = (state, { match }) => {
  const courseId = parseInt(match.params.courseId);
  const course = selectCourse(state.entities, courseId);
  return {
    courseId,
    course,
  };
};

const mapDispatchToProps = dispatch => ({
  fetchCourse: id => dispatch(fetchCourse(id))
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(CourseShow);
