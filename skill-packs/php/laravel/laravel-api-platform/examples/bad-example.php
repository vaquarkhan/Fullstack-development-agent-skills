// BAD — raw request, returns Eloquent model
public function store(Request $request) {
    return Order::create($request->all());
}
