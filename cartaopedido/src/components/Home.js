import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import CardList from "./CardList";
import NewCardModal from "./NewCardModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    cards: []
  };

  componentDidMount() {
    this.resetState();
  }

  getCards = () => {
    axios.get(API_URL).then(res => this.setState({ cards: res.data }));
  };

  resetState = () => {
    this.getCards();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <CardList
              cards={this.state.cards}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewCardModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;