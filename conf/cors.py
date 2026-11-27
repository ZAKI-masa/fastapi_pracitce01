from fastapi.middleware.cors import CORSMiddleware

# appを受け取って、CORSの設定を追加する関数
def set_up(app):
  # CORSミドルウェアを追加
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],  # すべてのオリジンを許可(本番環境では特定のオリジンのみを許可することをお勧めします)
      allow_methods=["*"],  # すべてのHTTPメソッドを許可
      allow_headers=["*"],  # すべてのヘッダーを許可
  )
