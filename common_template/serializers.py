def blog_to_json(blog):
    return {
        'id': blog.id,
        'title': blog.title,
        'text': blog.text,
        'views': blog.views,
        'create_at': blog.create_at,
    }
