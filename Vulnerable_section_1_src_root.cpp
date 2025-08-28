         c->setStash(QStringLiteral("cms_head"), QVariant::fromValue(safe));
     }
 
    const QString cms_foot = settings.value(QStringLiteral("cms_head"));
     if (!cms_foot.isEmpty()) {
         const Grantlee::SafeString safe(cms_foot, true);
         c->setStash(QStringLiteral("cms_foot"), QVariant::fromValue(safe));