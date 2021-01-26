
////
//
// Course API Utilities
//
////

// Course index API
export const fetchCourses = data => (
  $.ajax({
    method: 'GET',
    url: '/api/courses',
    data
  })
);

// Show individual course API
export const fetchCourse = id => (
  $.ajax({
    method: 'GET',
    url: '/api/courses/${id}'
  })
);

// Create course API
export const createCourse = courseForm => (
  $.ajax({
    method: 'POST',
    url: '/api/courses',
    data: courseForm,
    contentType: false,
    processData: false
  })
);

// Edit course API
export const updateCourse = courseForm => (
  $.ajax({
    method: 'PATCH',
    url: '/api/courses/${id}',
    data: courseForm,
    contentType: false,
    processData: false
  })
);

// Delete course API
export const destroyCourse = () => (
  $.ajax({
    method: 'DELETE',
    url: '/api/courses/${id}'
  })
);
