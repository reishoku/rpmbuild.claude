
%global baseurl https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases

%{!?_version: %global _version %(jq -r '.[]."@anthropic-ai/claude-code"' package.json)}

%define __arch_install_post %{nil}
%define __os_install_post %{nil}

Name:           claude-code
Version:        2.0.50
Release:        1%{?dist}
Summary:        Claude Code

License:        Proprietary
URL:            https://claude.ai

BuildRequires: jq

Recommends: epel-release
Requires: ripgrep

Provides: claude
Provides: claude-code

%ifarch x86_64
%global claude_arch linux-x64
%endif
%ifarch aarch64
%global claude_arch linux-arm64
%endif

Source0:  %{baseurl}/%{version}/%{claude_arch}/claude
Source10: claude-wrapper

%description
Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows -- all through natural language commands.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}

%{__mkdir_p} %{buildroot}%{_libexecdir}/%{name}
%{__install} -m 0755 %{SOURCE0}  %{buildroot}%{_libexecdir}/%{name}/claude-code
%{__install} -m 0755 %{SOURCE10} %{buildroot}%{_bindir}/claude

%files
%{_bindir}/claude
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/claude-code

%changelog
* Sat Nov 22 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.50-1
- Update to 2.0.50

* Sat Nov 22 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.49-1
- Update to 2.0.49

* Thu Nov 20 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.47-1
- Update to 2.0.47

* Wed Nov 19 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.46-1
- Update to 2.0.46

* Wed Nov 19 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.45-1
- Update to 2.0.45

* Tue Nov 18 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.44-1
- Update to 2.0.44

* Sun Nov 16 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.42-1
- Update to 2.0.42

* Sat Nov 15 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.41-1
- Update to 2.0.41

* Tue Nov 11 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.37-1
- Update to 2.0.37

* Tue Nov 04 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.32-1
- Update to 2.0.32

* Tue Nov 04 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.31-3
- Disable telemetry related environmental variables, again
- Make use of system-provided ripgrep (available in EPEL)

* Mon Nov 03 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.31-2
- Disable telemetry related environmental variables
- Add aarch64 GitHub Actions workflow for CI
- Modify spec file

* Sat Nov 01 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.31-1
- Initial RPM package for Claude Code
