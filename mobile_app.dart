import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: Home()));

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[800],
      appBar: AppBar(
        title: Text("Welcome to the Univerisity!"),
        backgroundColor: Colors.black,
        centerTitle: true,
      ),
      body: Column(
        children: [
          Container(
            padding: EdgeInsets.fromLTRB(90, 10, 16, 6),
            child: Text(
              "Please select who you are:",
              style: TextStyle(
                fontSize: 20,
                color: Colors.white
              ),
            ),
          ),
          Container(
            padding: EdgeInsets.fromLTRB(90, 70, 16, 20),
            child: FlatButton(
              onPressed: () {},
              child: Text(
                'Student',
                style: TextStyle(
                  fontSize: 30,
                  color: Colors.white
                ),
              ),
              color: Colors.grey[900],
              minWidth: 145,
            ),
          ),
          Container(
            padding: EdgeInsets.fromLTRB(90, 70, 16, 20),
            child: FlatButton(
              onPressed: () {},
              child: Text(
                'Teacher',
                style: TextStyle(
                    fontSize: 30,
                    color: Colors.white
                ),
              ),
              color: Colors.grey[900],
              minWidth: 145,
            ),
          ),
          Container(
            padding: EdgeInsets.fromLTRB(90, 70, 16, 20),
            child: FlatButton(
              onPressed: () {},
              child: Text(
                'Admin',
                style: TextStyle(
                    fontSize: 30,
                    color: Colors.white
                ),
              ),
              color: Colors.grey[900],
              minWidth: 145,
            ),
          ),
          Container(
            padding: EdgeInsets.fromLTRB(90, 70, 16, 20),
            child: FlatButton(
              onPressed: () {},
              child: Text(
                'Parent',
                style: TextStyle(
                    fontSize: 30,
                    color: Colors.white
                ),
              ),
              color: Colors.grey[900],
              minWidth: 145,
            ),
          )
        ],
      )

      );
  }
}
