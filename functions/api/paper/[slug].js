/**
 * functions/api/paper/[slug].js — R2 Content Proxy
 * 
 * Fetches markdown papers from R2 (server-side, no CORS needed)
 * and returns them to the client. Decouples content (R2) from 
 * presentation (Pages template).
 */
export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  
  // Extract slug from /api/paper/[slug]
  const slug = url.pathname.replace(/^\/api\/paper\//, '').replace(/\/$/, '');
  
  if (!slug) {
    return new Response('Missing paper slug', { status: 400 });
  }
  
  // Fetch from R2 (server-side — no CORS restrictions)
  const r2Url = `https://pub-426be63219f54be3932467bcbaf805f5.r2.dev/papers/${slug}.md`;
  
  try {
    const r2Response = await fetch(r2Url);
    
    if (!r2Response.ok) {
      return new Response('Paper not found', { status: 404 });
    }
    
    const content = await r2Response.text();
    
    return new Response(content, {
      headers: {
        'Content-Type': 'text/markdown; charset=utf-8',
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'public, max-age=3600'
      }
    });
  } catch (e) {
    return new Response(`Error fetching paper: ${e.message}`, { status: 500 });
  }
}
