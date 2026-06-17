// BAD — http call in widget, no error handling, dynamic JSON
ElevatedButton(
  onPressed: () async {
    final r = await http.post(Uri.parse('$base/orders'), body: jsonEncode(fields));
    setState(() => order = jsonDecode(r.body));
  },
  child: Text('Submit'),
)
