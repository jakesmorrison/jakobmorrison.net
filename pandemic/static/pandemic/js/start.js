

var cardStyle = {
    background: "grey",
    border:  "1px solid #ccc",
    borderRadius: "3px",
    width: "200px",
    height: "350px"
}


var InfectionDeck = React.createClass({
    getInitialState: function(){
        return {
            in_de: 30
        }
    },
    handleChange: function(e){
        this.setState({
            in_de: this.state.in_de - 1
        });
    },
    render: function(){
        return (
            <div style = {cardStyle}>
                Number here: {this.state.in_de} <br />
                <input type="button" value="Draw Card" onClick={this.handleChange} />
            </div>
        )
    }
});

var InfectionDiscard = React.createClass({
    getInitialState: function(){
        return {
            in_di: 0
        }
    },
    handleChange: function(e){
        this.setState({
            in_di: this.in_di + 1
        });
    },
    render: function(){
        return (
            <div style = {cardStyle}>
                Number here: {this.state.in_di} <br />
            </div>
        )
    }
});


ReactDOM.render(
  <InfectionDeck />,
  document.getElementById('infectionDeck')
);


ReactDOM.render(
  <InfectionDiscard />,
  document.getElementById('infectionDiscard')
);

//var infectionDiscard =
//
//var actionDeck =
//
//var actionDiscard =