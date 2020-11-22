import React, { Component } from 'react';

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src="https://kontaazul.com.br/wp-content/uploads/2019/07/unnamed.png"
          width="300"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        />
        <hr/>
        <h5>
          <i>Apresenta</i>
        </h5>
        <h1>Solicitação de Cartão de Crédito</h1>
      </div>
    );
  }
}

export default Header;