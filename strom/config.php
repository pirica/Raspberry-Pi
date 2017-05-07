<?php
/*
 * Raspberry Remote
 * http://xkonni.github.com/raspberry-remote/
 *
 * configuration for the webinterface
 *
 */

/*
 * define ip address and port here
 */
$source = $_SERVER['SERVER_ADDR'];
$target = '192.168.178.26';
$port = 11337;

/*
 * specify configuration of sockets to use
 *   array("systemcode", "group" , "plug", "description");
 * use empty string to create empty box
 *   ""
 *
 */
$config=array(
    /*
     * Elro
     */
    array("1", "-ausgeblendet-", "16", "Bett Lampe"),
    array("1", "-ausgeblendet-", "08", "LED-Strip"),
    array("1", "-ausgeblendet-", "04", "Schreibtisch Lampe"),
#  array("1", "-ausgeblendet-", "02", "Nr. 4"),
#  array("1", "-ausgeblendet-", "01", "Nr. 5"),
    /*
     * Intertech
     */
#  array("2", "01", "01", "IT 1"),
#  array("2", "01", "02", "IT 2"),
#  array("2", "01", "03", "IT 3"),
#  array("2", "01", "04", "IT 4"),
)
?>
