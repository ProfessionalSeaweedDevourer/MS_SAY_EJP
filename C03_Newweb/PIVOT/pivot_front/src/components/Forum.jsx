import React, { useContext, useState } from 'react';
import { UserContext } from '../context/UserContext';

const Avatar = ({ name, src, size = 40 }) => {
  const [imgError, setImgError] = useState(false);
  const initial = name ? name.charAt(0).toUpperCase() : '?';
  if (src && !imgError) return <img src={src} alt={name} className="rounded-full" style={{ width: size, height: size, objectFit: 'cover' }} onError={() => setImgError(true)} />;
  return (
    <div className="rounded-full bg-slate-300 text-slate-700 flex items-center justify-center font-semibold" style={{ width: size, height: size }}>{initial}</div>
  );
};

const Forum = () => {
  const { userInfo, setUserInfo } = useContext(UserContext);
  const [posts, setPosts] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [newPost, setNewPost] = useState('');
  const POSTS_PER_PAGE = 5;

  React.useEffect(() => {
    const load = async () => {
      try {
        const res = await fetch('http://localhost:8000/posts');
        if (res.ok) {
            const data = await res.json();
            setPosts(data);
            setCurrentPage(1);
          }
      } catch (e) { console.error(e); }
    };
    load();
  }, []);

  const handleCreatePost = async () => {
    if (!userInfo?.name) return alert('로그인한 사용자만 게시글을 작성할 수 있습니다.');
    if (!newPost.trim()) return;
    try {
      const res = await fetch(`http://localhost:8000/posts`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ content: newPost.trim() }),
      });
      if (!res.ok) {
        const err = await res.json();
        return alert(err.detail || '게시 생성 실패');
      }
      setNewPost('');
      setCurrentPage(1);
      // refresh posts
      const list = await fetch('http://localhost:8000/posts');
      if (list.ok) {
        const data = await list.json();
        setPosts(data);
        setCurrentPage(1);
      }
      // refresh user counts
      const profile = await fetch(`http://localhost:8000/users/${userInfo.id}`);
      if (profile.ok) {
        const profileJson = await profile.json();
        setUserInfo((prev) => ({ ...prev, ...profileJson }));
      }
    } catch (e) {
      console.error(e);
      alert('서버와 통신할 수 없습니다.');
    }
  };

  const handleAddComment = async (postId, text) => {
    if (!userInfo?.name) return alert('로그인 후 댓글을 작성하세요.');
    if (!text.trim()) return;
    try {
      const res = await fetch(`http://localhost:8000/posts/${postId}/comments`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ content: text.trim() }),
      });
      if (!res.ok) {
        const err = await res.json();
        return alert(err.detail || '댓글 달기 실패');
      }
      // refresh posts and user counts
      const list = await fetch('http://localhost:8000/posts');
      if (list.ok) setPosts(await list.json());
      const profile = await fetch(`http://localhost:8000/users/${userInfo.id}`);
      if (profile.ok) {
        const profileJson = await profile.json();
        setUserInfo((prev) => ({ ...prev, ...profileJson }));
      }
    } catch (e) {
      console.error(e);
      alert('서버와 통신할 수 없습니다.');
    }
  };

  const handleDeletePost = async (postId) => {
    if (!confirm('정말 이 게시글을 삭제하시겠습니까?')) return;
    try {
      const res = await fetch(`http://localhost:8000/posts/${postId}`, { method: 'DELETE', credentials: 'include' });
      if (!res.ok) {
        const err = await res.json();
        return alert(err.detail || '게시글 삭제 실패');
      }
      const list = await fetch('http://localhost:8000/posts');
      if (list.ok) setPosts(await list.json());
      const profile = await fetch(`http://localhost:8000/users/${userInfo.id}`);
      if (profile.ok) {
        const profileJson = await profile.json();
        setUserInfo((prev) => ({ ...prev, ...profileJson }));
      }
    } catch (e) {
      console.error(e);
      alert('서버와 통신할 수 없습니다.');
    }
  };

  const handleDeleteComment = async (postId, commentId) => {
    if (!confirm('정말 이 댓글을 삭제하시겠습니까?')) return;
    try {
      const res = await fetch(`http://localhost:8000/posts/${postId}/comments/${commentId}`, { method: 'DELETE', credentials: 'include' });
      if (!res.ok) {
        const err = await res.json();
        return alert(err.detail || '댓글 삭제 실패');
      }
      const list = await fetch('http://localhost:8000/posts');
      if (list.ok) setPosts(await list.json());
      const profile = await fetch(`http://localhost:8000/users/${userInfo.id}`);
      if (profile.ok) {
        const profileJson = await profile.json();
        setUserInfo((prev) => ({ ...prev, ...profileJson }));
      }
    } catch (e) {
      console.error(e);
      alert('서버와 통신할 수 없습니다.');
    }
  };

  return (
    <div className="space-y-6">
      <div className="bg-white p-4 rounded shadow-sm border border-slate-200">
        <h2 className="text-lg font-semibold mb-3">Forum</h2>

        <div className="flex gap-3">
          <div className="flex-shrink-0">
            <Avatar name={userInfo?.name} src={userInfo?.profileImage} size={48} />
          </div>
          <div className="flex-1">
            <textarea
              value={newPost}
              onChange={(e) => setNewPost(e.target.value)}
              placeholder={userInfo?.name ? '짧은 게시글을 작성하세요.' : '로그인해야 글을 작성할 수 있습니다.'}
              className="w-full p-3 border border-slate-300 rounded resize-none h-24"
              disabled={!userInfo?.name}
            />
            <div className="flex justify-end mt-2">
              <button
                className={`px-4 py-2 rounded font-semibold ${userInfo?.name ? 'bg-blue-600 text-white hover:bg-blue-700' : 'bg-slate-200 text-slate-500 cursor-not-allowed'}`}
                onClick={handleCreatePost}
                disabled={!userInfo?.name}
              >
                게시
              </button>
            </div>
          </div>
        </div>
      </div>

      <div className="space-y-4">
        {posts.length === 0 && (
          <div className="text-center text-slate-500 p-8 bg-white rounded border">아직 게시글이 없습니다. 첫 번째 글을 남겨보세요.</div>
        )}

        {/* current page slice */}
        {(() => {
          const totalPages = Math.max(1, Math.ceil(posts.length / POSTS_PER_PAGE));
          const start = (currentPage - 1) * POSTS_PER_PAGE;
          const end = start + POSTS_PER_PAGE;
          const pagePosts = posts.slice(start, end);
          return pagePosts.map((pst) => (
            <div key={pst.id} className="bg-white p-4 rounded shadow-sm border border-slate-200">
              <div className="flex gap-3">
                <div className="flex-shrink-0"><Avatar name={pst.author_name} src={pst.author_profile} /></div>
                <div className="flex-1">
                  <div className="flex items-center justify-between">
                    <div>
                      <div className="font-semibold">{pst.author_name}</div>
                      <div className="text-xs text-slate-400">{new Date(pst.created_at).toLocaleString()}</div>
                    </div>
                  </div>
                  <div className="mt-3 text-slate-800 whitespace-pre-wrap">{pst.content}</div>

                  <div className="mt-4 border-t pt-3">
                    <CommentsBlock post={pst} onAddComment={handleAddComment} onDeleteComment={handleDeleteComment} currentUser={userInfo} />
                  </div>
                </div>
              </div>
            </div>
          ));
        })()}

        {/* pagination controls */}
        {posts.length > POSTS_PER_PAGE && (
          <div className="flex justify-center mt-4">
            <div className="inline-flex items-center gap-2">
              <button
                className="px-2 py-1 rounded bg-slate-100"
                onClick={() => setCurrentPage((p) => Math.max(1, p - 1))}
                disabled={currentPage === 1}
              >Prev</button>

              {Array.from({ length: Math.ceil(posts.length / POSTS_PER_PAGE) }, (_, i) => i + 1).map((num) => (
                <button
                  key={num}
                  onClick={() => setCurrentPage(num)}
                  className={`px-3 py-1 rounded ${currentPage === num ? 'bg-blue-600 text-white' : 'bg-white border'}`}
                >{num}</button>
              ))}

              <button
                className="px-2 py-1 rounded bg-slate-100"
                onClick={() => setCurrentPage((p) => Math.min(Math.ceil(posts.length / POSTS_PER_PAGE), p + 1))}
                disabled={currentPage === Math.ceil(posts.length / POSTS_PER_PAGE)}
              >Next</button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

const CommentsBlock = ({ post, onAddComment, onDeleteComment, currentUser }) => {
  const [commentText, setCommentText] = useState('');
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    if (!onAddComment) return;
    if (!commentText.trim()) return;
    setLoading(true);
    try {
      await onAddComment(post.id, commentText.trim());
      setCommentText('');
    } catch (e) {
      console.error(e);
      alert('댓글 작성 중 오류가 발생했습니다.');
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (commentId) => {
    if (!onDeleteComment) return;
    if (!confirm('정말 이 댓글을 삭제하시겠습니까?')) return;
    try {
      await onDeleteComment(post.id, commentId);
    } catch (e) {
      console.error(e);
      alert('댓글 삭제 중 오류가 발생했습니다.');
    }
  };

  return (
    <div className="space-y-3">
      {Array.isArray(post.comments) && post.comments.map((c) => (
        <div key={c.id} className="flex gap-3 items-start">
          <div className="flex-shrink-0"><img src={c.author_profile || ''} alt={c.author_name} className="rounded-full" style={{ width: 32, height: 32, objectFit: 'cover' }} onError={(e) => { e.target.style.display = 'none'; }} /></div>
          <div className="flex-1 bg-slate-50 p-2 rounded">
            <div className="flex justify-between items-start">
              <div className="text-sm font-semibold">{c.author_name} <span className="text-xs text-slate-400 font-normal">{new Date(c.created_at).toLocaleString()}</span></div>
              <div>
                {currentUser?.id === c.author_id && (
                  <button onClick={() => handleDelete(c.id)} className="text-xs text-red-600 hover:underline">삭제</button>
                )}
              </div>
            </div>
            <div className="text-sm text-slate-700">{c.content}</div>
          </div>
        </div>
      ))}

      <div className="flex gap-3 items-start">
        <div className="flex-shrink-0">
          <img src={currentUser?.profileImage || ''} alt={currentUser?.name} className="rounded-full" style={{ width: 32, height: 32, objectFit: 'cover' }} onError={(e) => { e.target.style.display = 'none'; }} />
        </div>
        <div className="flex-1">
          <textarea
            value={commentText}
            onChange={(e) => setCommentText(e.target.value)}
            placeholder={currentUser?.name ? '댓글을 입력하세요.' : '로그인 후 댓글 작성이 가능합니다.'}
            className="w-full p-2 border border-slate-200 rounded resize-none h-16"
            disabled={!currentUser?.name || loading}
          />
          <div className="flex justify-end mt-2">
            <button
              onClick={submit}
              disabled={!currentUser?.name || loading}
              className={`px-3 py-1 rounded font-semibold ${currentUser?.name ? 'bg-blue-600 text-white' : 'bg-slate-200 text-slate-500 cursor-not-allowed'}`}
            >댓글</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Forum;
