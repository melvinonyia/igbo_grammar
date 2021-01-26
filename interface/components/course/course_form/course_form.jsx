
////
//
// Class Form Presentation Component
//
////

import React from 'react';
import { withRouter } from 'react-router';

class ClassForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      description: '',
    };
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  update(property) {
    return e => this.setState({
      [property]: e.target.value
    });
  }

  // This will be where we create our form data to submit our photo
  handleSubmit(e) {
    e.preventDefault();
    const formData = new FormData();
    formData.append('bench[description]', this.state.description);
    this.props.createBench(formData);
  }

  render() {
    const { description } = this.state;

    return (
      <div className="new-class-container">
        <div className="new-class-form">
          <h3 className="new-class-title">Create A Class</h3>

          <form onSubmit={this.handleSubmit}>
            <label className="bench-field">Description</label>
            <input
              type="text"
              value={description}
              onChange={this.update('description')}
              className="bench-field"
            />

            <hr />

            <div className="button-holder">
              <input
                type="submit"
                value="Create Class"
                className="new-class-button"
              />
            </div>
          </form>

          <div className="button-holder">
            <button
              className="new-class-button"
              onClick={this.navigateToSearch}
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    );
  }
}

export default withRouter(ClassForm);
