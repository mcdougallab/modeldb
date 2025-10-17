"""
Middleware for URL normalization in ModelDB.

This middleware normalizes URLs by:
1. Removing the 'modeldb/' prefix from paths
2. Removing '.html' and '.cshtml' extensions

This approach preserves POST data unlike redirect-based solutions.
"""


class URLNormalizationMiddleware:
    """
    Middleware to normalize URLs without redirecting.
    
    This rewrites request.path before routing occurs, so it works
    seamlessly with both GET and POST requests.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Normalize the path
        original_path = request.path
        normalized_path = self.normalize_path(original_path)
        
        # If the path changed, rewrite it
        if normalized_path != original_path:
            request.path = normalized_path
            request.path_info = normalized_path
        
        response = self.get_response(request)
        return response
    
    def normalize_path(self, path):
        """
        Normalize a URL path by removing modeldb/ prefix and file extensions.
        
        Args:
            path: The URL path to normalize
            
        Returns:
            The normalized path
        """
        # Remove leading slash for processing
        clean_path = path.lstrip('/')
        
        # Remove 'modeldb/' prefix (case insensitive)
        if clean_path.lower().startswith('modeldb/'):
            clean_path = clean_path[8:]  # len('modeldb/') = 8
        
        # Remove .html or .cshtml extensions (case insensitive)
        lower_path = clean_path.lower()
        if lower_path.endswith('.html'):
            clean_path = clean_path[:-5]  # len('.html') = 5
        elif lower_path.endswith('.cshtml'):
            clean_path = clean_path[:-7]  # len('.cshtml') = 7
        
        # Re-add leading slash
        return '/' + clean_path if clean_path else '/'
