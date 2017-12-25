/**
 * Created by deepbay on 2017/12/14.
 */
'use strict';

var React = require('react');
var AMUIReact = require('amazeui-react');
var Nav = AMUIReact.Nav;
var NavItem = AMUIReact.NavItem;

var LeftBar = React.createClass({

    componentDidMount: function () {

    },

    render: function () {
        return <Nav>
            <NavItem active href="http://www.amazeui.org" >首页</NavItem>
            <NavItem href="./pages/manager/add.html">开始使用</NavItem>
            <NavItem href="http://www.amazeui.org">按需定制</NavItem>
        </Nav>;
    }

});

module.exports = LeftBar;
