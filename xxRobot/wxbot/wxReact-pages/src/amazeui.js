/**
 * Created by deepbay on 2017/12/13.
 */
var React = require('react');
var ReactDOM = require('react-dom');
var AMUIReact = require('amazeui-react');
var Button = AMUIReact.Button;

var LeftBar = require('./components/framework/LeftBar')

ReactDOM.render(<Button amStyle={"primary"}>Butotn</Button>, document.getElementById("div"));

ReactDOM.render(<LeftBar ></LeftBar>,document.getElementById("leftbar"));