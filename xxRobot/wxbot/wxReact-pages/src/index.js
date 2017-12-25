/**
 * Created by deepbay on 2017/12/13.
 */
var React = require('react');
var ReactDOM = require('react-dom');
var AMUIReact = require('amazeui-react');

var LeftBar = require('./components/framework/LeftBar');
var Title = require('./components/framework/Title');

ReactDOM.render(<LeftBar ></LeftBar>,document.getElementById("leftbar"));
ReactDOM.render(<Title ></Title>,document.getElementById("title"));