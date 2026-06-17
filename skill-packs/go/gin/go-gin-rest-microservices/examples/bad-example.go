// BAD — global DB, no context, string errors
func Create(c *gin.Context) {
    db.Exec("INSERT INTO orders ...")
    c.JSON(200, "ok")
}
